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
});
