#include <iostream>
#include <windows.h>
int main(int argc, char* argv[]) {
	if (argc != 2) {
		std::cerr << "Usage: exe.exe <id>" << std::endl;
		return 1;
	}
	int id = std::atoi(argv[1]);
	HANDLE semaphore = OpenSemaphore(SEMAPHORE_MODIFY_STATE, FALSE, L"MySemaphore");
	if (semaphore == NULL) {
		std::cerr << "Failed to open semaphore. Error code: " << GetLastError() << std::endl;
		return 1;
	}
	std::cout << "Child process with id " << id << " started." << std::endl;
	int rand = std::rand() % 2000 + 10000;
	Sleep(rand);
	std::cout << "Child process with id " << id << " completed." << std::endl;
	ReleaseSemaphore(semaphore, 1, NULL);
	CloseHandle(semaphore);
	return 0;
}