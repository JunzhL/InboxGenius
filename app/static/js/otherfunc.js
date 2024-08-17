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

// Fetch or generate your email data (this is just an example)
// function loadEmails(input_emails) {
//     saveEmailsToLocalStorage(input_emails);
//     renderEmails();
// }

// Function to render emails on the current page
// function renderEmails() {
//     const emails = loadEmailsFromLocalStorage();
//     const start = (currentPage - 1) * itemsPerPage;
//     const end = start + itemsPerPage;
//     const paginatedEmails = emails.slice(start, end);

//     // const emailList = document.querySelector('.email-items');
//     // emailList.innerHTML = '';

//     var emailList = $('.email-list ul.list-group');
//     emailList.empty(); // Clear the current list

//     paginatedEmails.forEach(function(email) {
//       var date = new Date(email.created_at);
//       var formattedDate = (date.getMonth() + 1) + '/' + date.getDate() + '/' + date.getFullYear();
//       var emailItem = `
//           <li class="list-group-item d-flex justify-content-between align-items-center email-item" data-id="${email._id}">
//               <div class="email-info">
//                   <h6>${email.sender_info.name}</h6>
//                   <p class="mb-1">${email.subject}</p>
//                   <small>${email.preview}</small>
//               </div>
//               <small>${formattedDate}</small>
//           </li>
//       `;
//       emailList.append(emailItem);
//   });

    // paginatedEmails.forEach(email => {
    //     const emailItem = document.createElement('li');
    //     emailItem.classList.add('list-group-item');
    //     emailItem.innerHTML = `<strong>${email.subject}</strong>`;
    //     emailItem.onclick = () => showEmailContent(email.content);
    //     emailList.appendChild(emailItem);
    // });
// }

// Function to show email content when clicked
// function showEmailContent(content) {
//     const emailContent = document.getElementById('email-content');
//     emailContent.innerHTML = `<p>${content}</p>`;
// }

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
    alert(currentPage * itemsPerPage);
    if (currentPage * itemsPerPage < loadEmailsFromLocalStorage().length) {
        currentPage++;
        savePageToLocalStorage(currentPage);
        populateEmailList();
    }
}

// Initialize the email list
// loadEmails();
