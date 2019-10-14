function changeCellState(cell, socket){
/*
Toggles the state of the table element (cell).
Sends the coordinates of the changed cell to the server.
*/
    cell.classList.toggle('alive');
    socket.emit('updateCell', {'x': cell.getAttribute('x'), 'y': cell.getAttribute('y')})
}

function createGrid(n_rows, n_columns, socket) {
/*
Creates a click-able grid (table) where the td elements can take on two states, either alive (className = 'alive')
or not alive (no className).
*/
    var grid = document.createElement('table');
    grid.className = 'grid';
    for (var j=0; j<n_rows; ++j) {
        var tr = grid.appendChild(document.createElement('tr'));
        for (var i=0; i<n_columns; ++i) {
            var td = grid.appendChild(document.createElement('td'));
            td.setAttribute('x', i);
            td.setAttribute('y', j);
            td.id = i + j*n_columns;
            td.addEventListener('click', function(td) {
                changeCellState(td.target, socket);
            });
        }
    }
    return grid;
}

function createStartButton(socket) {
/*
Creates a button that on click, sends a signal to the server to start (or resume) the grid evolutions.
*/
    var btn = document.createElement('button');
    btn.innerHTML = 'start';
    btn.addEventListener('click', function() {
        socket.emit('start')
        console.log('start')
    });
    return btn;
}

function createStopButton(socket) {
/*
Creates a button that on click, sends a signal to the server to pause the grid evolutions.
*/
    var btn = document.createElement('button');
    btn.innerHTML = 'stop';
    btn.addEventListener('click', function() {
        socket.emit('stop')
        console.log('stop')
    });
    return btn;
}

function createResetButton(socket) {
/*
Creates a button that on click, sends a signal to the server to resets the grid to a random state.
*/
    var btn = document.createElement('button');
    btn.innerHTML = 'reset';
    btn.addEventListener('click', function() {
        socket.emit('reset')
        console.log('reset');
    });
    return btn;
}

function updateGrid(msg) {
/*
Updates each td element using the JSON msg from the server.
*/
   $('td').each(function(){
        var id = $(this).attr('id');

        if (msg[id] == 1){
            $(this).addClass('alive');
        } else {
            $(this).removeClass('alive');
        }
   });
}

$(document).ready(function(){
    var socket = io.connect('http://' + document.domain + ':' + location.port);
    var start_btn = createStartButton(socket);
    var reset_btn = createResetButton(socket);
    var stop_btn = createStopButton(socket);
    document.body.appendChild(start_btn)
    document.body.appendChild(reset_btn)
    document.body.appendChild(stop_btn)
    var grid = createGrid(40, 40, socket);
    document.body.appendChild(grid);
    socket.on('nextState', function(msg){
        updateGrid(msg)
    });
});