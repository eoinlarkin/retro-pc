
# Testing

## Non Functional Tests
- Is the email console backend disabled ?
- Is debug mode deactivated ?

## Functionality Tests
- Can a user without an account make an order
- If I delete a user account can I still view the order history ?
- Can I manually upload a product
- Can I purchase the uploaded product
- Do all messages render correctly on the site?

## Add Product Form
- Can add new product using form
- Check that the if an invalid field is submitted the form will return an error
    - Check that for numeric fields the number of digits corresponds to the database definition
- Form is only accessible if the user is a superuse
- Images can be added successfully through the form
- Products that have been added manually can be added to the cart
    - May need to include if statement logic if the image does not render correctly
