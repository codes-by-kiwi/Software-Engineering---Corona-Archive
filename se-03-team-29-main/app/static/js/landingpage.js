var visitor = $("#login_data").data("visitor");
var place = $("#login_data").data("place");
var agent = $("#login_data").data("agent");
var hospital = $("#login_data").data("hospital");

function href_setter(account) {
  $("#proceedbtn").click(() => {
    if (account == "agent") redirector("/agent_home");
    if (account == "hospital") redirector("/hospital_home");
    if (account == "visitor") redirector("/visitor_home");
    if (account == "place") redirector("/place_home");
  });
}

function redirector(dir) {
  window.location = dir;
}

function check_logged_in(form) {
  if (form == "agent" && agent !== "None") {
    $("#agent_hospital_form").css("display", "none");
    $("#signed_in").css("display", "flex");
    $("#account_type").html("Agent");
    href_setter("agent");
  } else if (form == "hospital" && hospital !== "None") {
    $("#agent_hospital_form").css("display", "none");
    $("#signed_in").css("display", "flex");
    $("#account_type").html("Hospital");
    href_setter("hospital");
  } else if (form == "visitor" && visitor !== "None") {
    $("#visitor_form").css("display", "none");
    $("#signed_in").css("display", "flex");
    $("#account_type").html("Visitor");
    href_setter("visitor");
  } else if (form == "place" && place !== "None") {
    $("#place_form").css("display", "none");
    $("#signed_in").css("display", "flex");
    $("#account_type").html("Place Owner");
    href_setter("place");
  } else {
    $("#signed_in").css("display", "none");
  }

  switch (form) {
    case "agent":
      $("#agentbtn").addClass("btnblue_pressed");
      $("#hospitalbtn").removeClass("btnblue_pressed");
      $("#visitorbtn").removeClass("btngrey_pressed");
      $("#placebtn").removeClass("btngrey_pressed");
      break;
    case "hospital":
      $("#agentbtn").removeClass("btnblue_pressed");
      $("#hospitalbtn").addClass("btnblue_pressed");
      $("#visitorbtn").removeClass("btngrey_pressed");
      $("#placebtn").removeClass("btngrey_pressed");
      break;
    case "visitor":
      $("#agentbtn").removeClass("btnblue_pressed");
      $("#hospitalbtn").removeClass("btnblue_pressed");
      $("#visitorbtn").addClass("btngrey_pressed");
      $("#placebtn").removeClass("btngrey_pressed");
      break;
    case "place":
      $("#agentbtn").removeClass("btnblue_pressed");
      $("#hospitalbtn").removeClass("btnblue_pressed");
      $("#visitorbtn").removeClass("btngrey_pressed");
      $("#placebtn").addClass("btngrey_pressed");
      break;
  }
}

check_logged_in("agent");

function agent_login_ajax() {
  $.post(
    "/agent_login",
    {
      username: $("#agent_hospital_username").val(),
      password: $("#agent_hospital_password").val(),
    },
    (response, fail) => {
      if (response == "Success") window.location.href = "/agent_home";
      else {
        $(".agent_hospital_error").css("display", "initial");
        $(".agent_hospital_error").html("Wrong username or password");
      }
    }
  );
}

function hospital_login_ajax() {
  $.post(
    "/hospital_login",
    {
      username: $("#agent_hospital_username").val(),
      password: $("#agent_hospital_password").val(),
    },
    (response) => {
      if (response == "Success") window.location.href = "/hospital_home";
      else {
        $(".agent_hospital_error").css("display", "initial");
        $(".agent_hospital_error").html("Wrong username or password");
      }
    }
  );
}

function agent_login() {
  $("#agent_hospital_form").css("display", "flex");
  $(".agent_hospital_error").css("display", "none");
  $("#agent_hospital_btn").attr("onclick", "agent_login_ajax()");
  $("#visitor_form").css("display", "none");
  $("#place_form").css("display", "none");
  check_logged_in("agent");
}

function hospital_login() {
  $("#agent_hospital_form").css("display", "flex");
  $(".agent_hospital_error").css("display", "none");
  $("#agent_hospital_btn").attr("onclick", "hospital_login_ajax()");
  $("#visitor_form").css("display", "none");
  $("#place_form").css("display", "none");
  check_logged_in("hospital");
}

function visitor_register() {
  $("#agent_hospital_form").css("display", "none");
  $("#visitor_form").css("display", "flex");
  $("#place_form").css("display", "none");
  check_logged_in("visitor");
}

function place_register() {
  $("#agent_hospital_form").css("display", "none");
  $("#visitor_form").css("display", "none");
  $("#place_form").css("display", "flex");
  check_logged_in("place");
}

const visitor_email = document.getElementById("visitor_email");
const visitor_phone = document.getElementById("visitor_phone");

visitor_email.addEventListener("change", () => {
  if ($("#visitor_email").val() != "")
    $("#visitor_phone").removeAttr("required");
  else $("#visitor_phone").attr("required");
});

visitor_phone.addEventListener("change", () => {
  if ($("#visitor_phone").val() != "")
    $("#visitor_email").removeAttr("required");
  else $("#visitor_email").attr("required");
});
