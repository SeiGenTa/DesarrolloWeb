/*
 * This is the JavaScript function that makes the example work. Note that
 * this script defines the calculate() function called by the event
 * handlers in the form. The function reads values from the form
 * <input> fields using the names defined in the HTML code above.  It outputs
 * its results into the named <span> elements.
 */
function calculate() {
    // Get the user's input from the form. Assume it is all valid.
    // Convert interest from a percentage to a decimal, and convert from
    // an annual rate to a monthly rate. Convert payment period in years
    // to the number of monthly payments.
    var principal = document.loandata.principal.value;
    var interest = document.loandata.interest.value / 100 / 12;
    var payments = document.loandata.years.value * 12;

    // Now compute the monthly payment figure, using esoteric math.
    var x = Math.pow(1 + interest, payments);
    var monthly = (principal*x*interest)/(x-1);

    // Get named <span> elements from the form.
    var payment = document.getElementById("payment");
    var total = document.getElementById("total");
    var totalinterest = document.getElementById("totalinterest");

    // Check that the result is a finite number. If so, display the
    // results by setting the HTML content of each <span> element.
    if (isFinite(monthly)) {
        payment.innerHTML = monthly.toFixed(2);
        total.innerHTML = (monthly * payments).toFixed(2);
        totalinterest.innerHTML = ((monthly*payments)-principal).toFixed(2);
    }
    // Otherwise, the user's input was probably invalid, so display nothing.
    else {
        payment.innerHTML = "";
        total.innerHTML = ""
        totalinterest.innerHTML = "";
    }
}
