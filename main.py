def main():
  ## This variable will contain a list of expenses
  expenses = []
  ## This variable will store the result of a function get_mortgage()
  mortgage = get_mortgage()
  expenses.append(mortgage)

  ## This variable will store the result of a function get_student_loans()
  student_loans = get_student_loans()
  expenses.append(student_loans)

  ## This variable will store the result of a function get_personal_loans()
  personal_loans = get_personal_loans()
  expenses.append(personal_loans)

  ## This variable will store the result of a function get_car_loan()
  car_loan = get_car_loan()
  expenses.append(car_loan)

  ## This variable will store the result of a function get_credit_cards()
  credit_card_payments = get_credit_cards()
  expenses.append(credit_card_payments)

  ## This variable will store the result of a function get_other_recurring()
  other_recurring = get_other_recurring()
  expenses.append(other_recurring)

  ## This variable will store the result of a function get_gross_income()
  gross_income = get_gross_income()

  ## This variable will store the result of a function get_total_payments() that will return the total payments.
  monthly_total = get_total_payments(expenses)

  ## This variable will store the result of a function get_dti() that will return the debt to income percentage.
  debt_to_income = get_dti(monthly_total, gross_income)

  ## This will print the debt_to_income to the screen
  print('Your debt to income ratio is ' + str(debt_to_income) + '%')

## This function will return the value of a user input morgage value.
## It will test for both numeric and positive values.
def get_mortgage():
  mortgage = 0.00

  while True:
      mortgage = input('Enter your monthly mortgage: ')
      is_number = mortgage.isnumeric() 
      if is_number:
          mortgage = float(mortgage)
          if mortgage >= 0:
            return mortgage

## This function will return the value of a user input student loan value.
## It will test for both numeric and positive values.
def get_student_loans():
  student_loan = 0.00

  while True:
      student_loan = input('Enter your monthly student loan payment: ')
      is_number = student_loan.isnumeric()
      if is_number:
        student_loan = float(student_loan)
        if student_loan >= 0:
          return student_loan

## This function will return the value of a user input personal loan value.
## It will test for both numeric and positive values.
def get_personal_loans():
  personal_loan = 0.00

  while True:
      personal_loan = input('Enter your monthly personal loan payment: ')
      is_number = personal_loan.isnumeric()
      if is_number:
        personal_loan = float(personal_loan)
        if personal_loan >= 0:
          return personal_loan

## This function will return the value of a user input car loan value.
## It will test for both numeric and positive values.
def get_car_loan():
  car_loan = 0.00

  while True:
      car_loan = input('Enter your monthly car payment: ')
      is_number = car_loan.isnumeric()
      if is_number:
        car_loan = float(car_loan)
        if car_loan >= 0:
          return car_loan

## This function will return the value of a user input credit card value.
## It will test for both numeric and positive values.
def get_credit_cards():
  credit_cards = 0.00

  while True:
      credit_cards = input('Enter your monthly credit card payment: ')
      is_number = credit_cards.isnumeric()
      if is_number:
        credit_cards = float(credit_cards)
        if credit_cards >= 0:
          return credit_cards

## This function will return the value of a user other recurring expense value.
## It will test for both numeric and positive values.
def get_other_recurring():
  other_recurring = 0.00

  while True:
      other_recurring = input(
          'Enter your monthly recurring expenses not in any of the other categories.: ')
      is_number = other_recurring.isnumeric()
      if is_number:
        other_recurring = float(other_recurring)
        if other_recurring >= 0:
          return other_recurring

## This function will prompt for the value of a user gross income.
## It will test for both numeric and positive values.
def get_gross_income():
  gross_income = 0.00

  while True:
      gross_income = input('Enter your monthly gross income: ')
      is_number = gross_income.isnumeric()
      if is_number:
        gross_income = float(gross_income)
        if gross_income >= 0:
          return gross_income

## This function will calculate the total sum of all expenses.
def get_total_payments(expenses):
  total_payments = sum(expenses)
  return total_payments

## This function will calculate the current debt to income ratio and return that value
def get_dti(monthly_total, gross_income):
  dti = (monthly_total / gross_income) * 100

  return dti

## This will start the program 
main()