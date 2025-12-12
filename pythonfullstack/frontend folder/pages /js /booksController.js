function loadBooks() {
    fetch(API_URL)
        .then(res => res.json())
        .then(data => {
            let rows = "";
            data.forEach(b => {
                rows += `
                    <tr>
                        <td>${b.id}</td>
                        <td>${b.title}</td>
                        <td>${b.author}</td>
                        <td>${b.year}</td>
                        <td>
                            <button onclick="deleteBook(${b.id})">Delete</button>
                        </td>
                    </tr>
                `;
            });
            document.querySelector("#booksTable tbody").innerHTML = rows;
        });
}

function addBook() {
    const book = {
        title: document.getElementById("title").value,
        author: document.getElementById("author").value,
        year: document.getElementById("year").value,
    };

    fetch(API_URL, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(book)
    }).then(() => loadBooks());
}

function deleteBook(id) {
    fetch(API_URL + id, { method: "DELETE" })
        .then(() => loadBooks());
}

loadBooks();
