$(document).ready(function() {
    // Initialize the app by fetching emails
    fetchEmails();

    // Event listener for email items (this needs to be attached after the emails are loaded)
    $(document).on('click', '.email-item', function() {
        var emailId = $(this).data('id');
        loadEmailContent(emailId);
    });

    $(document).on('click', '.btn-gen-email', function() {
        generateEmail();
    });

    $(document).on('click', '.flagged-emails-btn', function() {
        fetchFlagEmails();
    });

    $(document).on('click', '.all-emails-btn', function() {
        
        fetchEmails();
    });

    $('.search-box input').on('keypress', function(e) {
        if (e.which === 13) {
            var query_text = $(this).val().trim();
            if (query_text) {
                aiSearch(query_text);
            } else {
                alert('Please enter search text.');
            }
        }
    });
});
