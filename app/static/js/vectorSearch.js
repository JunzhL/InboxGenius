function aiSearch(query_text) {
    localStorage.setItem('vectorSearch', true);
    // limit = localStorage.getItem('emails');
    // limit = JSON.parse(limit).length;
    limit = localStorage.getItem('vectorSearchLimit');
    // console.log("Limit type: ", typeof limit);
    // console.log("Limit: ", limit);

    $.ajax({
        type: 'POST',
        url: '/find_emails',
        contentType: 'application/json',
        data: JSON.stringify({ 
            search_text: query_text,
            limit: limit
         }),
        success: function(response) {
            console.log("Vector search response: ", response);
            localStorage.setItem('vectorSearch-result', JSON.stringify(response));
            populateEmailList();
            console.log("Email list populated after vec search.");
        },
        error: function() {
            console.log('Error searching emails.');
        }
    });
}