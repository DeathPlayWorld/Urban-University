import time
import threading


def write_words(word_count, file_name):
    file = open(file_name, "w", encoding="utf-8")
    for word in range(1, word_count+1):
        file.write(f"Some word № {word}\n")
        time.sleep(0.1)
    print(f"Function end writing in {file_name}")

#Functions
func_start_time = time.time()

write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")

func_end_time = time.time()
print(f"\nFunctions operated: {round((func_end_time - func_start_time), 2)} s\n")

#Threads
thread_start_time = time.time()

threads = [] #List of threads to save space
input_list = [(10, "example5.txt"), (30, "example6.txt"), (200, "example7.txt"), (100, "example8.txt")] #Arguments for write_words()

#Starting threads
for argument in input_list:
    thread = threading.Thread(target=write_words, args=argument)
    threads.append(thread)
    thread.start()

#Waiting every thread to end
for thread in threads:
    thread.join()

thread_end_time = time.time()
print(f"\nThreads operated: {round((thread_end_time - thread_start_time), 2)} s\n")