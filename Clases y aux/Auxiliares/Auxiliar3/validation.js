const validateEmail = (email) => {
  if (!email) return false;
  // length validation
  let lengthValid = email.length > 15;

  // format validation
  let re = /^[\w.]+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$/;
  let formatValid = re.test(email);

  // return logic AND of validations.
  return lengthValid && formatValid;
};

const validatePhoneNumber = (phoneNumber) => {
  if (!phoneNumber) return false;
  // length validation
  let lengthValid = phoneNumber.length >= 8;

  // format validation
  let re = /^[0-9]+$/;
  let formatValid = re.test(phoneNumber);

  // return logic AND of validations.
  return lengthValid && formatValid;
};

const validateFiles = (files) => {
  if (!files) return false;

  // number of files validation
  let lengthValid = 1 <= files.length && files.length <= 3;

  // file type validation
  let typeValid = true;

  for (const file of files) {
    // file.type should be "image/<foo>" or "application/pdf"
    let fileFamily = file.type.split("/")[0];
    typeValid &&= fileFamily == "image" || file.type == "application/pdf";
  }

  // return logic AND of validations.
  return lengthValid && typeValid;
};

const validateForm = () => {
  // get elements from DOM by using form's name.
  let myForm = document.forms["myForm"];
  let email = myForm["email"].value;
  let phoneNumber = myForm["phone"].value;
  let files = myForm["files"].files;

  // validation auxiliary variables and function.
  let invalidInputs = [];
  let isValid = true;
  const setInvalidInput = (inputName) => {
    invalidInputs.push(inputName);
    isValid &&= false;
  };

  // validation logic
  if (!validateEmail(email)) {
    setInvalidInput("Email");
  }
  if (!validatePhoneNumber(phoneNumber)) {
    setInvalidInput("Phone number");
  }
  if (!validateFiles(files)) {
    setInvalidInput("Picture(s)");
  }

  // finally display validation
  let validationBox = document.getElementById("val-box");
  let validationMessageElem = document.getElementById("val-msg");
  let validationListElem = document.getElementById("val-list");

  if (!isValid) {
    validationListElem.textContent = "";
    // add invalid elements to val-list element.
    for (input of invalidInputs) {
      let listElement = document.createElement("li");
      listElement.innerText = input;
      validationListElem.append(listElement);
    }
    // set val-msg
    validationMessageElem.innerText = "Los siguiente campos son invalidos:";

    // make validation prompt visible
    validationBox.hidden = false;
  } else {
    myForm.submit();
  }
};

let submitBtn = document.getElementById("submit-btn");
submitBtn.addEventListener("click", validateForm);
