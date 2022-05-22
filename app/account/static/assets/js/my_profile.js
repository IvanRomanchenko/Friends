function delEvent(el) {
    el.addEventListener('click', function() {
        el.parentElement.parentElement.remove();
    });
}


function delAlert() {
    document.getElementById('alert_status').remove();
}


window.addEventListener('load', function() {

    // eventListener for add_contact button
    document.getElementById('add_contact').addEventListener('click', function() {
        var contact_li = document.getElementById('id_li_contacts_0').cloneNode(true);
        var contact_input = contact_li.querySelector('input[id=id_contacts_0]');
        var contact_del_btn = contact_li.querySelector('button[name=del_contact]');

        var items = document.getElementsByName('li_contacts');
        var last_item = items[items.length - 1];
        var next_id = items.length + 1;

        contact_li.removeAttribute('hidden');
        contact_li.setAttribute('id', 'id_li_contacts_' + next_id);
        contact_input.setAttribute('name', 'contacts');
        contact_input.setAttribute('id', 'id_contacts_' + next_id);

        delEvent(contact_del_btn);

        last_item.parentElement.append(contact_li);
    });

    // eventListener for del_contact button
    document.getElementsByName('del_contact').forEach(function(el) {
        delEvent(el);
    });

    setTimeout(delAlert, 6000);
});
