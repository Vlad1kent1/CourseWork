#include <iostream>
#include <windows.h>
#include <locale>
#include <codecvt>
#include <string>
const int NUM_PROCESSES = 10;
const int MAX_RUNNING_PROCESSES = 3;
void HandleError(const char* errorMessage) {
	std::cerr << errorMessage << " (Error code: " << GetLastError() << ")" << std::endl;
}
int main() {
	SECURITY_ATTRIBUTES securityAttributes;
	securityAttributes.nLength = sizeof(SECURITY_ATTRIBUTES);
	securityAttributes.lpSecurityDescriptor = NULL;
	securityAttributes.bInheritHandle = TRUE;
	HANDLE mutex = CreateMutex(&securityAttributes, FALSE, L"MyMutex");
	if (mutex == NULL) {
		std::cerr << "Failed to create mutex. Error code: " << GetLastError() << std::endl;
		return 1;
	}
	HANDLE semaphore = CreateSemaphore(&securityAttributes, MAX_RUNNING_PROCESSES,
		MAX_RUNNING_PROCESSES, L"MySemaphore");
	if (semaphore == NULL) {
		std::cerr << "Failed to create semaphore. Error code: " << GetLastError() << std::endl;
		CloseHandle(mutex);
		return 1;
	}
	HANDLE timer = CreateWaitableTimer(&securityAttributes, TRUE, L"MyTimer");
	if (timer == NULL) {
		std::cerr << "Failed to create timer. Error code: " << GetLastError() << std::endl;
		CloseHandle(mutex);
		CloseHandle(semaphore);
		return 1;
	}
	if (WaitForSingleObject(mutex, INFINITE) != WAIT_OBJECT_0) {
		HandleError("Failed to acquire mutex");
		CloseHandle(mutex);
		CloseHandle(semaphore);
		CloseHandle(timer);
		return 1;
	}
	std::wcout << L"Main process started." << std::endl;
	HANDLE childProcesses[NUM_PROCESSES];
	for (int i = 0; i < NUM_PROCESSES; ++i) {
		if (WaitForSingleObject(semaphore, INFINITE) != WAIT_OBJECT_0) {
			HandleError("Failed to wait for semaphoreee");
			ReleaseMutex(mutex);
			CloseHandle(mutex);
			CloseHandle(semaphore);
			CloseHandle(timer);
			return 1;
		}
		std::wstring wideCommandLine = L"exe.exe " + std::to_wstring(i);
		PROCESS_INFORMATION processInfo;
		STARTUPINFO startupInfo;
		ZeroMemory(&startupInfo, sizeof(startupInfo));
		startupInfo.cb = sizeof(startupInfo);
		LPWSTR commandLineArray = const_cast<LPWSTR>(wideCommandLine.c_str());
		if (CreateProcess(NULL, commandLineArray, NULL, NULL, FALSE, 0, NULL, NULL, &startupInfo,
			&processInfo)) {
			std::wcout << L"Child process " << i << L" created." << std::endl;
			CloseHandle(processInfo.hThread);
			childProcesses[i] = processInfo.hProcess;
		}
		else {
			HandleError("Failed to create process");
		}
	}
	WaitForMultipleObjects(NUM_PROCESSES, childProcesses, TRUE, 5000);
	ReleaseMutex(mutex);
	LARGE_INTEGER dueTime;
	dueTime.QuadPart = -50000000LL; // 5 секунд
	if (!SetWaitableTimer(timer, &dueTime, 0, NULL, NULL, FALSE)) {
		HandleError("Failed to set timer");
	}
	if (WaitForSingleObject(timer, INFINITE) != WAIT_OBJECT_0) {
		HandleError("Failed to wait for timer");
	}
	CloseHandle(mutex);
	CloseHandle(semaphore);
	CloseHandle(timer);
	std::wcout << L"Main process completed." << std::endl;
	return 0;
}
