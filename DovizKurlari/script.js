$(document).ready(function() {
    // Function to fetch and update data
    function fetchData() {
        $.ajax({
            url: 'today.xml',
            dataType: 'xml',
            success: function(data) {
                // Parse XML data and extract the information you need
                var tableData = '<table style="width:100%; border-collapse: collapse; margin-top: 20px;"><tr style="background-color: #f2f2f2;"><th style="padding: 8px; text-align: left;">Currency</th><th style="padding: 8px; text-align: left;">ForexBuying</th><th style="padding: 8px; text-align: left;">ForexSelling</th><th style="padding: 8px; text-align: left;">BanknoteBuying</th><th style="padding: 8px; text-align: left;">BanknoteSelling</th></tr>'; // Table header

                $(data).find('Currency').each(function() {
                    var currencyName = $(this).find('Isim').text();
                    var forexBuying = $(this).find('ForexBuying').text();
                    var forexSelling = $(this).find('ForexSelling').text();
                    var BanknoteBuying = $(this).find('BanknoteBuying').text();
                    var BanknoteSelling = $(this).find('BanknoteSelling').text();

                    // Add a new row to the table for each currency
                    tableData += `<tr style="border-bottom: 1px solid #ddd;"><td style="padding: 8px;">${currencyName}</td><td style="padding: 8px;">${forexBuying}</td><td style="padding: 8px;">${forexSelling}</td><td style="padding: 8px;">${BanknoteBuying}</td><td style="padding: 8px;">${BanknoteSelling}</td></tr>`;
                });

                tableData += '</table>'; // Close the table

                // Update the HTML content with the new table data
                $('#dataDisplay').html(tableData);
            },
            error: function(xhr, status, error) {
                console.error('Error fetching data:', error);
            }
        });
    }

    // Initial fetch and then update every 10 seconds
    fetchData();
    setInterval(fetchData, 10000);  // Refresh every 10 seconds (10000 milliseconds)
});
