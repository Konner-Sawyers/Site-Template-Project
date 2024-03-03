function retrieve_project(fileName){
    console.log(fileName);
    $.ajax({
        method: "GET",
        url: "/get_project_file",
        data: {nameOfFile: fileName},
        success: function(data){
            $("#project-viewer-id").html(data.result)
        }
    })
}