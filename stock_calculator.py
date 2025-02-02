class StockCalculator:
    def __init__(self, buy_price, sell_price, quantity, brokerage_rate=0.4, capital_gains_tax=5):
        """
        Initialize the calculator with stock transaction details.
        :param buy_price: Price per share at the time of purchase (in NPR).
        :param sell_price: Price per share at the time of sale (in NPR).
        :param quantity: Number of shares.
        :param brokerage_rate: Brokerage fee as a percentage (default 0.4%).
        :param capital_gains_tax: Capital gains tax as a percentage (default 5%).
        """
        self.buy_price = buy_price
        self.sell_price = sell_price
        self.quantity = quantity
        self.brokerage_rate = brokerage_rate / 100  # Convert to decimal
        self.capital_gains_tax = capital_gains_tax / 100  # Convert to decimal

    def calculate_buy_cost(self):
        """Calculate total cost of buying shares including brokerage."""
        base_cost = self.buy_price * self.quantity
        brokerage = base_cost * self.brokerage_rate
        total_buy_cost = base_cost + brokerage
        return round(total_buy_cost, 2)

    def calculate_sell_revenue(self):
        """Calculate total revenue from selling shares after deducting brokerage."""
        base_revenue = self.sell_price * self.quantity
        brokerage = base_revenue * self.brokerage_rate
        total_sell_revenue = base_revenue - brokerage
        return round(total_sell_revenue, 2)

    def calculate_profit_loss(self):
        """Calculate profit or loss after considering all costs."""
        total_buy_cost = self.calculate_buy_cost()
        total_sell_revenue = self.calculate_sell_revenue()
        profit_loss = total_sell_revenue - total_buy_cost
        return round(profit_loss, 2)

    def calculate_profit_loss_percentage(self):
        """Calculate profit/loss as a percentage of the total buy cost."""
        total_buy_cost = self.calculate_buy_cost()
        profit_loss = self.calculate_profit_loss()
        profit_loss_percentage = (profit_loss / total_buy_cost) * 100
        return round(profit_loss_percentage, 2)

    def calculate_capital_gains_tax(self):
        """Calculate capital gains tax on the profit."""
        profit_loss = self.calculate_profit_loss()
        if profit_loss > 0:
            capital_gains_tax = profit_loss * self.capital_gains_tax
        else:
            capital_gains_tax = 0
        return round(capital_gains_tax, 2)

    def generate_report(self):
        """Generate a detailed report of the transaction."""
        total_buy_cost = self.calculate_buy_cost()
        total_sell_revenue = self.calculate_sell_revenue()
        profit_loss = self.calculate_profit_loss()
        profit_loss_percentage = self.calculate_profit_loss_percentage()
        capital_gains_tax = self.calculate_capital_gains_tax()

        report = {
            "Total Buy Cost (NPR)": total_buy_cost,
            "Total Sell Revenue (NPR)": total_sell_revenue,
            "Profit/Loss (NPR)": profit_loss,
            "Profit/Loss (%)": profit_loss_percentage,
            "Capital Gains Tax (NPR)": capital_gains_tax,
        }
        return report