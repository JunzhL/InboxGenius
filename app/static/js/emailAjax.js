function fetchEmails() {
    $.ajax({
        url: '/emails', // Endpoint to fetch emails
        method: 'GET',
        success: function(response) {
            saveEmailsToLocalStorage(response);
            savePageToLocalStorage(1);
            populateEmailList(response);
        },
        error: function() {
            $('.email-list').html('<p>Error loading email list.</p>');
        }
    });
}

function fetchFlagEmails() {
    $.ajax({
        url: '/emails/flagged',
        method: 'GET',
        success: function(response) {
            saveEmailsToLocalStorage(response);
            savePageToLocalStorage(1);
            populateEmailList(response);
        },
        error: function() {
            $('.email-list').html('<p>Error loading flagged emails.</p>');
        }
    });
}

function populateEmailList() {
    emails = sliceEmails(loadEmailsFromLocalStorage(), loadPageFromLocalStorage());
    var emailList = $('.email-list ul.list-group');
    emailList.empty(); // Clear the current list
    emails.forEach(function(email) {
        var date = new Date(email.created_at);
        var formattedDate = (date.getMonth() + 1) + '/' + date.getDate() + '/' + date.getFullYear();
        var emailItem = `
            <li class="list-group-item d-flex justify-content-between align-items-center email-item" data-id="${email._id}">
                <div class="email-info">
                    <h6>${email.sender_info.name}</h6>
                    <p class="mb-1">${email.subject}</p>
                    <small>${email.preview}</small>
                </div>
                <small>${formattedDate}</small>
            </li>
        `;
        emailList.append(emailItem);
    });
}

function loadEmailContent(emailId) {
    $.ajax({
        url: '/emails/' + emailId,
        method: 'GET',
        success: function(response) {
            var date = new Date(response.created_at);
            var formattedDate = `${(date.getMonth() + 1).toString().padStart(2, '0')}/${date.getDate().toString().padStart(2, '0')}/${date.getFullYear()} ${date.getHours().toString().padStart(2, '0')}:${date.getMinutes().toString().padStart(2, '0')}` + (date.getHours() >= 12 ? ' PM' : ' AM');
            $('#email-content').html(`
                <h4>${response.subject}</h4>
                <div class="email-header d-flex justify-content-between align-items-center">
                    <div>
                        <h6>${response.sender_info.name}</h6>
                        <small>${formattedDate}</small>
                    </div>
                </div>
                <div class="email-body mt-3">
                    <p>${response.content}</p>
                </div>
            `);
        },
        error: function() {
            $('#email-content').html('<p>Error loading email content.</p>');
        }
    });
}

function generateEmail() {
    $.ajax({
        url: '/emails/generated',
        method: 'GET',
        success: function(response) {
            fetchEmails();
            loadEmailContent(response._id);
        },
        error: function() {
            alert('Error generating email.');
        }
    });
}

// function fetchEmails() {
    
// }