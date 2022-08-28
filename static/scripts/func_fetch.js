

let select_zona = document.getElementById('zona_id');
select_zona.addEventListener('change', function () {
    zona_id = document.getElementById('zona_id').value;
    select_area = document.getElementById('area_id');

    fetch("{% url 'ajax_load_areas' %}?zona_id=".concat(zona_id)).then(function (response) {
        if (response.status == 200) {
            response.text().then(function (t) {
                select_area.innerHTML = t;
            })
        } else {
            alert('Não foi possível buscar areas');
        }
    })
})


let select_area = document.getElementById('area_id');
select_area.addEventListener('change', function () {
    let area_id = document.getElementById('area_id').value;
    let select_cong = document.getElementById('congregacao_id');

    fetch("{% url 'ajax_load_congregacoes' %}?area_id=".concat(area_id)).then(function (response) {
        if (response.status == 200) {
            response.text().then(function (t) {
                select_cong.innerHTML = t;
            })
        }
    })
})



let btn_buscar = document.getElementById("buscar_id");
let area_lista = document.getElementById("area_lista");

btn_buscar.addEventListener('click', function () {
    let nome = document.getElementById("nome_input").value;
    let select_zona = document.getElementById("zona_id").value;
    let select_area = document.getElementById("area_id").value;
    let select_cong = document.getElementById("congregacao_id").value;
    let select_cargo = document.getElementById("cargo_id").value;


    fetch("{% url 'pesquisar_pessoas' %}?"
        .concat("pesquisa_nome=").concat(nome)
        .concat("&zona_id=").concat(select_zona)
        .concat('&area_id=').concat(select_area)
        .concat("&congregacao_id=").concat(select_cong)
        .concat("&cargo_id=").concat(select_cargo))
        .then(function (response) {

            if (response.status == 200) {
                response.text().then(function (t) {
                    area_lista.innerHTML = t;
                })
            } else {
                alert('Falha na busca');
            }
        });

})





