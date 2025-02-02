document.getElementById('calculate-btn').addEventListener('click', async () => {
    const buyPrice = document.getElementById('buy_price').value;
    const sellPrice = document.getElementById('sell_price').value;
    const quantity = document.getElementById('quantity').value;
    const brokerageRate = document.getElementById('brokerage_rate').value;
    const capitalGainsTax = document.getElementById('capital_gains_tax').value;

    // Show loading indicator
    document.getElementById('loading-indicator').style.display = 'block';
    document.getElementById('result').style.display = 'none';

    try {
        const response = await fetch('/calculate/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                buy_price: parseFloat(buyPrice),
                sell_price: parseFloat(sellPrice),
                quantity: parseInt(quantity),
                brokerage_rate: parseFloat(brokerageRate),
                capital_gains_tax: parseFloat(capitalGainsTax),
            }),
        });

        const data = await response.json();

        document.getElementById('total_buy_cost').textContent = data['Total Buy Cost (NPR)'];
        document.getElementById('total_sell_revenue').textContent = data['Total Sell Revenue (NPR)'];
        document.getElementById('profit_loss').textContent = data['Profit/Loss (NPR)'];
        document.getElementById('profit_loss_percentage').textContent = data['Profit/Loss (%)'];
        document.getElementById('capital_gains_tax_result').textContent = data['Capital Gains Tax (NPR)'];

        document.getElementById('result').style.display = 'block';
    } catch (error) {
        alert('An error occurred while calculating. Please try again.');
    } finally {
        document.getElementById('loading-indicator').style.display = 'none';
    }
});