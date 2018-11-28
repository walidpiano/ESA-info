$(document).ready(function() {
    $("#login-form").submit(function(event) {
        event.preventDefault();
        
        var studentName;
        var esaNumber;
        var dateOfBirth;

        esaNumber = $('#esa-number').val();
        studentName = $('#student-name').val();
        dateOfBirth = $('#birth-date').val();
        if (dateOfBirth != '' & (esaNumber != '' || studentName != '')) {
            GetData(studentName, esaNumber, dateOfBirth);
        }
    });
        

    $('.modalDialog').click(function(){
        ShowHideMessage(false);
    })

});

function GetData(studentName, esaNumber, dateOfBirth) {

    studentInfo = {
        "name": studentName,
        "date_of_birth": dateOfBirth,
        "esa_number": esaNumber
    }
    
    $.ajax({
        type: "PUT",
        url: "get/instructor",
        data: JSON.stringify(studentInfo),
        contentType: "application/json; charset=UTF-8",
        dataType: "json",
        success: function(response) {
            console.log(response);
            result = response['result'];
            if (result) {
                $('#esa-number').val('');
                $('#student-name').val('');
                $('#birth-date').val('');
                window.location = '/instructor/' + result;
            } else {
                console.log('false');
                //window.location = '/#openModal';
                ShowHideMessage(true);
            }
        },
        error: function(error) {
            console.log(error);
            result = false;
        }
    });
}

function ShowHideMessage(showOrHide) {
    if (showOrHide) {
        $('.modalDialog').addClass('to-show');
    } else {
        $('.modalDialog').removeClass('to-show');
    }
}