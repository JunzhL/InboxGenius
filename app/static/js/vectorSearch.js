function aiSearch(query_text) {
    $.ajax({
        type: 'POST',
        url: '/find_emails',
        contentType: 'application/json',
        data: JSON.stringify({ search_text: query_text }),
        success: function(response) {
            console.log("Vector search response: ", response);
        },
        error: function() {
            console.log('Error searching emails.');
        }
    });
}