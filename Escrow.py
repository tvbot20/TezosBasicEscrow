import smartpy as sp
@sp.module
def main():
    class SimpleEscrow(sp.Contract):
        def __init__(self):
            self.data.balance = sp.tez(0)
        @sp.entrypoint
        def deposit(self):
            self.data.balance += sp.amount
        @sp.entrypoint
        def claim(self, address, amount):
            sp.send(address, amount)
            self.data.balance -= amount
@sp.add_test(name="SimpleEscrow")
def test():
    scenario = sp.test_scenario(main)
    scenario.h1("Simple Escrow")
    alice = sp.test_account("Alice")
    bob = sp.test_account("Bob")
    c1 = main.SimpleEscrow()
    scenario += c1
    c1.deposit().run(sender=alice, amount=sp.tez(50))
    c1.claim(address=bob.address, amount=sp.tez(10)).run(sender=bob)

