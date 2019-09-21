var grid = createGrid(40, 40)
document.body.appendChild(grid)

function createGrid(n_rows, n_columns){
    var grid = document.createElement('table')
    grid.className = 'grid'
    for (var j=0; j<n_rows; ++j){
        var tr = grid.appendChild(document.createElement('tr'))
        for (var i=0; i<n_columns; ++i){
            var td = grid.appendChild(document.createElement('td'))
        }
    }
    return grid
}