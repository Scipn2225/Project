$(document).ready( function () {
    $('#myTable').DataTable(
        {
            "lenghtMenu" : [2,3,5,10,20],
            lenghtChange: true,
            info: true,
            pagelenght: 2
        }
    );
});


