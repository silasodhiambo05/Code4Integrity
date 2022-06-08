<?php
// Reads the variables sent via POST
$sessionId   = $_POST["sessionId"];  
$serviceCode = $_POST["serviceCode"];  
$text = $_POST["text"];
//This is the first menu screen
if ( $text == "" ) {
$response  = " CON Thankyou for contacting the EACC, this reporting line is anonymous,we would like to assure you of your safety";
$response .= "1. Enter 1 to continue";
}
// Menu for a user who selects '1' from the first menu
// Will be brought to this second menu screen
else if ($text == "1") {
$response  = " CON Please let us know what you are reporting  \n";
$response .= "1. Bid rigging \n";
$response .= "2. Collusive bidding \n";
$response .= "3. Phantom vendors \n";
$response .= "4. Corrupt Officials \n";
}
//Menu for a user who selects '1' from the second menu above
// Will be brought to this third menu screen
else if ($text == "1*1") {
$response = " CON You are about to report a Bid rigging incident \n";
$response .= "Would you like to add anything else? Please Enter 1 to confirm \n";
}
else if ($text == "1*1*1") {
$response = "CON Please give us more details,Thankyou for your Vigilance! \n";
$response .= "Enter 1 to continue \n";
$response .= "Enter 0 to cancel";
}
else if ($text == "1*1*1*1") {
$response = " END Your report has been successfully submitted!";
}
else if ($text == "1*1*1*0") {
$response = " END Your report has been withdrawn";
}
// Menu for a user who selects "2" from the second menu above
// Will be brought to this fourth menu screen
else if ($text == "1*2") {
$response = " CON You are about to report a Collusive bidding           \n";
$response .= "Please Enter 1 to confirm \n";
}
// Menu for a user who selects "1" from the fourth menu screen
else if ($text == "1*2*1") {
$response = " CON Please give us more details,Thankyou for your Vigilance! \n";
$response .= "Enter 1 to continue \n";
$response .= "Enter 0 to cancel";
}
else if ($text == "1*2*1*1") {
$response = "END Your report has been successfully submitted!";
}
else if ($text == "1*2*1*0") {
$response = "END Your report has been withdrawn";
}
// Menu for a user who enters "3" from the second menu above
// Will be brought to this fifth menu screen
else if ($text == "1*3") {
$response = "CON You are about to report a Phantom Vendors incident\n";
$response .= "Please Enter 1 to confirm \n";
}
// Menu for a user who enters "1" from the fifth menu
else if ($text == "1*3*1") {
$response = "CON Please give us more details,Thankyou for your Vigilance!  \n";
$response .= "Enter 1 to continue \n";
$response .= "Enter 0 to cancel";
}
else if ($text == "1*3*1*1") {
$response = " END Your report has been successfully submitted!";
}
else if ($text == "1*3*1*0") {
$response = " END Your report has been withdrawn";
}
// Menu for a user who enters "4" from the second menu above
// Will be brought to this sixth menu screen
else if ($text == "1*4") {
$response = "CON You are about to report a Corrupt Official incident \n";
$response .= "Please Enter 1 to confirm \n";
}
// Menu for a user who enters "1" from the sixth menu
else if ($text == "1*4*1") {
$response = " CON Please give us more details,Thankyou for your Vigilance!  \n";
$response .= "Enter 1 to continue \n";
$response .= "Enter 0 to cancel";
}
else if ($text == "1*4*1*1") {
$response = "END Your report has been successfully submitted!";
}
else if ($text == "1*4*1*0") {
$response = "END Your report has been withdrawn";
}
//echo response
header('Content-type: text/plain');
echo $response
?>