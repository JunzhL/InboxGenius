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

function populateEmailList(vectorSearch=false) {
    if (vectorSearch === true) {
        var emails = JSON.parse(localStorage.getItem('vectorSearch-result'));
        console.log("Vector search emails: ", emails);
    } else {
        emails = sliceEmails(loadEmailsFromLocalStorage(), loadPageFromLocalStorage());
        console.log("Current emails: ", emails);
    }
    
    var emailList = $('.email-list ul.list-group');
    emailList.empty();
    emails.forEach(function(email) {
        var date = new Date(email.created_at);
        var formattedDate = (date.getMonth() + 1) + '/' + date.getDate() + '/' + date.getFullYear();

        var date = (vectorSearch === true) ? '' : `<small>${formattedDate}</small>`;
        var score = vectorSearch && email.score ? `<small style="margin-left: 10px;"> ${email.score.toFixed(2)}</small>` : '';

        var emailItem = `
            <li class="list-group-item d-flex justify-content-between align-items-center email-item" data-id="${email._id}">
                <div class="email-info">
                    <h6>${email.subject}</h6>
                    <p class="mb-1">${email.sender_info.name}</p>
                </div>
                <div class="email-preview-container" style="display: none; position: absolute; top: 0; left: 0; width: 100%; border: 1px solid #ddd; padding: 10px; box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.1); z-index: 10;">
                    <p>${email.preview}</p>
                </div>
                ${date}${score}
            </li>
        `;
        emailList.append(emailItem);

        emailList.find('.email-item').last().hover(
            function() {
                $(this).find('.email-preview-container').show();
            },
            function() {
                $(this).find('.email-preview-container').hide();
            }
        );
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