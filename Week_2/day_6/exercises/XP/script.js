//EX1
//output 10

//Exo2
// to make the variablei undefined outside of the for loop
// function numbers() {
//     for (let i = 0; i < 5; i += 1) {
//       console.log(i);
//     }
//       console.log(i);
//   }
//   numbers();

  //Ex3
  let account = 2000;
  let vat;
  let expRev = {
      month: 12,
      year : 2020,
      expenses : 500,
      revenue : 1200
  }

  function expensesVat(expense) {
      return expense * 1.17;
  }

  function updateAccountRevenue(revenue) {
      return account = account + revenue;
  }

  function updateAccountExpense(expense) {
      return account = account - expense;
  }

  console.log (`On the month ${expRev["month"]}/${expRev["year"]} with a revenue of ${expRev["revenue"]} your account was credited of ${updateAccountRevenue(expRev["revenue"])}`);
  console.log (`Your exepenses VAT included were on ${expensesVat(expRev["expenses"])}`);
  vat = expensesVat(expRev["expenses"]);
  account = updateAccountExpense(vat);
  console.log (`Your account is now updated to ${account}`);
  
  