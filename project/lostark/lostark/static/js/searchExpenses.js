const searchField = document.querySelector('#searchField');
const tableOutput = document.querySelector('.table-output');
const appTable = document.querySelector('.app-table');
const paginationContainer = document.querySelector('.pagination-container');


tableOutput.style.display = 'none';

searchField.addEventListener('keyup', (e) =>{
    const searchValue = e.target.value;

    if (searchValue.trim().length > 0) {
        pagination-container.style.display = 'none';

        fetch("/search-expenses", {
            body: JSON.stringify({searchText: searchValue}),
            method: "POST",
        })
        .then((res) => res.json())
        .then((data) => {
            appTable.style.display = 'none';

            tableOutput.style.display = 'block';

            if (data.length == 0) {
                tableOutput.innerHTML = "No results found";
            }
        });
    }
});