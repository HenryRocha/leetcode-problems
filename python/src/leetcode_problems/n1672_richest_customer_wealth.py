class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        current_max_wealth: int = 0

        for account in range(len(accounts)):
            current_wealth = sum(accounts[account])

            if current_wealth > current_max_wealth:
                current_max_wealth = current_wealth

        return current_max_wealth
