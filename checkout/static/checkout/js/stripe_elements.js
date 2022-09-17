/*
    Stripe Integration Flow as follows:
    Step 01 -> Checkout View creates a Stripe PaymentIntent
    Step 02 -> Stripe returns a client_secret which is returned to the template
    Step 03 -> client_secret in the template used to call confirmCardPayment() and verify card
*/

/*
    Core logic/payment flow derived from Stripe Documentation:
    https://stripe.com/docs/payments/accept-card-payments?platform=web&ui=elements
    CSS from here: 
    https://github.com/stripe/elements-examples
*/

// Extracting the keys; slice function used to remove unused quoatation marks
var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();

console.log('Client secret:')
console.log(clientSecret)

console.log('Stripe Publick Key:')
console.log(stripePublicKey)

// style for card element
var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};

// Defining card for use in html code
var card = elements.create('card', {
    style: style
});

// Mounting the card element to the checkout page 
card.mount('#card-element');

// Handle realtime validation errors on the card element
// Errors are displayed next to the input form
card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});

// Handle form submit
var form = document.getElementById('payment-form');

form.addEventListener('submit', function (ev) {
    ev.preventDefault(); // preventing default action
    card.update({
        'disabled': true
    });
    $('#submit-button').attr('disabled', true);
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
    }).then(function (result) {
        if (result.error) {
            // checking for error with payment submission
            var errorDiv = document.getElementById('card-errors');
            var html = `
                <span class="icon" role="alert">
                <i class="fas fa-times"></i>
                </span>
                <span>${result.error.message}</span>`;
            $(errorDiv).html(html);
            // re-enabling the buttons to allow the user to resolve issue
            card.update({
                'disabled': false
            });
            $('#submit-button').attr('disabled', false);
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                // else we submit the form 
                form.submit();
            }
        }
    });
});