function activateLink(element) {
  // Remove 'active' class from all links
  const links = document.querySelectorAll(".nav-link");
  links.forEach((link) => link.classList.remove("active"));

  // Add 'active' class to the clicked link
  element.classList.add("active");
}

// const itemsPerPage = 10; // Adjust the number of emails per page
// // let emails = []; // This array will hold your email data

function saveEmailsToLocalStorage(emails) {
  localStorage.setItem('emails', JSON.stringify(emails));
}

// Load emails from local storage
function loadEmailsFromLocalStorage() {
  const storedEmails = localStorage.getItem('emails');
  console.log("Stored emails: ", storedEmails);
  return storedEmails ? JSON.parse(storedEmails) : [];
}

function savePageToLocalStorage(page) {
    localStorage.setItem('page', JSON.stringify(page));
}

function loadPageFromLocalStorage() {
    const storedPage = localStorage.getItem('page');
    return storedPage ? JSON.parse(storedPage) : 1;
}

function sliceEmails(emails, page) {
    const itemsPerPage = 10;
    const start = (page - 1) * itemsPerPage;
    const end = start + itemsPerPage;
    return emails.slice(start, end);
}

// Fetch o
// Handle Previous page button click
function prevPage() {
    currentPage = loadPageFromLocalStorage();
    if (currentPage > 1) {
        currentPage--;
        savePageToLocalStorage(currentPage);
        populateEmailList();
    }
}

// Handle Next page button click
function nextPage() {
    itemsPerPage = 10;
    currentPage = loadPageFromLocalStorage();
    if (currentPage * itemsPerPage < loadEmailsFromLocalStorage().length) {
        currentPage++;
        savePageToLocalStorage(currentPage);
        populateEmailList();
    }
}

// Initialize the email list
// loadEmails();
