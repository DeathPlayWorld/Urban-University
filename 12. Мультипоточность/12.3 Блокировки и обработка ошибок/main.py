import threading
import random
import time

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for operation in range(1, 101):
            increase = random.randint(50, 500)
            self.balance += increase
            print(f"Funding: {increase}. Balance: {self.balance}")
            time.sleep(0.001)
            if self.balance >= 500 and self.lock.locked(): self.lock.release()

    def take(self):
        for operation in range(1, 101):
            decrease = random.randint(50, 500)
            print(f"Request for {decrease}.")

            if self.balance >= decrease:
                self.balance -= decrease
                print(f"Withdrawal: {decrease}. Balance: {self.balance}")
                time.sleep(0.001)
            else:
                self.lock.acquire()
                print("\nRequest was blocked: Insufficient fund!\n")


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Final balance: {bk.balance}')