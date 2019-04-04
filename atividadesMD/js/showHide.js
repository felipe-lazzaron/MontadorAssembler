<script type="text/javascript">
    function showhide(e)
    {
        var div = e.parentNode.firstElementChild;

        if (div.style.display == "" || div.style.display == "none") {
            div.style.display = "block";
            e.setAttribute("class", "viewed");
            e.innerHTML = "Esconder Solução";
        } else {
            div.style.display = "none";
            e.innerHTML = "Ver Solução";
        }
    }
</script>