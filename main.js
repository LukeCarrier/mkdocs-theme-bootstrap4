import 'bootstrap';
import '@fortawesome/fontawesome-free/js/all';

import './main.scss';

$(function() {
  $('ul.dropdown-menu [data-toggle="dropdown"]').on('click', e => {
    const toggle = $(e.target);

    e.preventDefault();
    e.stopPropagation();

    toggle.parents('.dropdown-submenu').siblings().find('.show').removeClass('show');
    toggle.siblings().toggleClass('show');

    toggle.parents('li.nav-item.dropdown.show').on('hidden.bs.dropdown', function(e) {
      $('.dropdown-submenu .show').removeClass('show');
    });
  });

  $('#mkdocs-search-modal').on('shown.bs.modal', e => {
    $('#mkdocs-search-query').trigger('focus');
  });
});
