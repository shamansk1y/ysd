{% load static %}

<h3 class="mb-4 border-bottom pb-1">Filters</h3>

<!-- Форма для фильтров -->
<form id="filter-form"> <!-- Обернем фильтры в форму -->
  <!-- Фильтр по производителям -->
  <div class="card mb-4">
    <h6 class="card-header">Brands</h6>
    <div class="list-group list-group-flush">
      {% for brand in manufacturers_cat %}
      <li class="list-group-item">
        <input
          class="filter-checkbox"
          data-filter="manufacturer"
          value="{{ brand.id }}"
          type="checkbox"
          {% if brand.id in manufacturer_filters %}checked{% endif %}/>&nbsp;
        {{ brand.title }}
      </li>
      {% endfor %}
    </div>
  </div>

  <!-- Фильтр по весу -->
  <div class="card mb-4">
    <h6 class="card-header">Weight/Volume</h6>
    <div class="list-group list-group-flush">
      {% for weight in weights %}
      <li class="list-group-item">
        <input
          class="filter-checkbox"
          data-filter="weight"
          value="{{ weight }}"
          type="checkbox"
          {% if weight in weight_filters %}checked{% endif %}/>&nbsp;
        {{ weight }} OZ
      </li>
      {% endfor %}
    </div>
  </div>

  <!-- Фильтр по количеству пакетов в коробке -->
  <div class="card mb-4">
    <h6 class="card-header">Units per Case</h6>
    <div class="list-group list-group-flush">
      {% for bags in bags_in_case %}
      <li class="list-group-item">
        <input
          class="filter-checkbox"
          data-filter="bags"
          value="{{ bags }}"
          type="checkbox"
          {% if bags in bags_filters %}checked{% endif %}/>&nbsp;
        {{ bags }} ct
      </li>
      {% endfor %}
    </div>
  </div>

  <!-- Кнопка сброса всех фильтров -->
  <div class="text-center mt-4">
    <button type="button" id="reset-filters" class="btn btn-danger">Сбросить фильтры</button>
  </div>
</form>

<script>
document.addEventListener('DOMContentLoaded', function () {
    const filterCheckboxes = document.querySelectorAll('.filter-checkbox');
    const resetButton = document.getElementById('reset-filters');

    // Обработчик изменения чекбоксов
    filterCheckboxes.forEach(checkbox => {
        checkbox.addEventListener('change', function () {
            let params = new URLSearchParams(window.location.search);
            let filterType = this.getAttribute('data-filter');
            let filterValue = this.value;

            // Обновляем параметры запроса
            if (this.checked) {
                if (params.has(filterType)) {
                    params.set(filterType, params.get(filterType) + ',' + filterValue);
                } else {
                    params.append(filterType, filterValue);
                }
            } else {
                let values = params.get(filterType).split(',');
                values = values.filter(val => val !== filterValue);
                if (values.length > 0) {
                    params.set(filterType, values.join(','));
                } else {
                    params.delete(filterType);
                }
            }

            // Перезагружаем страницу с новыми параметрами
            window.location.search = params.toString();
        });
    });

    // Обработчик события для кнопки сброса всех фильтров
    resetButton.addEventListener('click', function() {
        // Сбросить все чекбоксы в форме
        const checkboxes = document.querySelectorAll('input[type="checkbox"]');
        checkboxes.forEach(checkbox => {
            checkbox.checked = false;
        });

        // Отправить форму для возврата к изначальному списку товаров
        const form = document.getElementById('filter-form');
        form.submit();
    });
});
</script>
