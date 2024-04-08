#include <iostream>
#include <Windows.h>
#include <string>

namespace MultiThreadedApp {
    const int NUM_PAIRS = 3;
    const int THREAD_COUNT = 2;
    const int NUM_NUMBERS = 500;

    CRITICAL_SECTION criticalSection;
    HANDLE hSemaphore;

    DWORD WINAPI PositiveThread(LPVOID lpParam) {
        int threadId = *((int*)lpParam);
        for (int i = 1; i <= NUM_NUMBERS; ++i) {
            WaitForSingleObject(hSemaphore, INFINITE);
            EnterCriticalSection(&criticalSection);
            std::cout << "Positive Thread " << threadId << ": " << i << std::endl;
            LeaveCriticalSection(&criticalSection);
            ReleaseSemaphore(hSemaphore, 1, NULL);
            // Записати у файл
            HANDLE hFile = CreateFile(TEXT("numbers.txt"), FILE_APPEND_DATA, FILE_SHARE_READ, NULL, OPEN_ALWAYS, FILE_ATTRIBUTE_NORMAL, NULL);
            if (hFile != INVALID_HANDLE_VALUE) {
                DWORD bytesWritten;
                WriteFile(hFile, std::to_string(i).c_str(), sizeof(char) * std::to_string(i).length(), &bytesWritten, NULL);
                WriteFile(hFile, "\r\n", sizeof(char) * 2, &bytesWritten, NULL);
                CloseHandle(hFile);
            }
        }
        return 0;
    }

    DWORD WINAPI NegativeThread(LPVOID lpParam) {
        int threadId = *((int*)lpParam);
        for (int i = -1; i >= -NUM_NUMBERS; --i) {
            WaitForSingleObject(hSemaphore, INFINITE);
            EnterCriticalSection(&criticalSection);
            std::cout << "Negative Thread " << threadId << ": " << i << std::endl;
            LeaveCriticalSection(&criticalSection);
            ReleaseSemaphore(hSemaphore, 1, NULL);
            // Записати у файл
            HANDLE hFile = CreateFile(TEXT("numbers.txt"), FILE_APPEND_DATA, FILE_SHARE_READ, NULL, OPEN_ALWAYS, FILE_ATTRIBUTE_NORMAL, NULL);
            if (hFile != INVALID_HANDLE_VALUE) {
                DWORD bytesWritten;
                WriteFile(hFile, std::to_string(i).c_str(), sizeof(char) * std::to_string(i).length(), &bytesWritten, NULL);
                WriteFile(hFile, "\r\n", sizeof(char) * 2, &bytesWritten, NULL);
                CloseHandle(hFile);
            }
        }
        return 0;
    }

    int main() {
        InitializeCriticalSection(&criticalSection);
        hSemaphore = CreateSemaphore(NULL, THREAD_COUNT, THREAD_COUNT, NULL);
        HANDLE threads[NUM_PAIRS][THREAD_COUNT];
        int threadIds[THREAD_COUNT];

        for (int i = 0; i < NUM_PAIRS; ++i) {
            threadIds[0] = i * 2 + 1;
            threadIds[1] = i * 2 + 2;
            for (int j = 0; j < THREAD_COUNT; ++j) {
                threads[i][j] = CreateThread(NULL, 0, j == 0 ? PositiveThread : NegativeThread, &threadIds[j], 0, NULL);
                if (threads[i][j] == NULL) {
                    // Обробка помилки
                    return 1;
                }
                SetThreadPriority(threads[i][j], i + THREAD_PRIORITY_BELOW_NORMAL);
                SuspendThread(threads[i][j]);
            }
        }

        for (int i = 0; i < NUM_PAIRS; ++i) {
            for (int j = 0; j < THREAD_COUNT; ++j) {
                ResumeThread(threads[i][j]);
            }
        }

        WaitForMultipleObjects(THREAD_COUNT, threads[0], TRUE, INFINITE);
        WaitForMultipleObjects(THREAD_COUNT, threads[1], TRUE, INFINITE);
        WaitForMultipleObjects(THREAD_COUNT, threads[2], TRUE, INFINITE);

        for (int i = 0; i < NUM_PAIRS; ++i) {
            for (int j = 0; j < THREAD_COUNT; ++j) {
                CloseHandle(threads[i][j]);
            }
        }

        CloseHandle(hSemaphore);
        DeleteCriticalSection(&criticalSection);

        return 0;
    }
}

int main() {
    return MultiThreadedApp::main();
}
