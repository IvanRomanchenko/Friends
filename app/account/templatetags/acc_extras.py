from django import template
from django.utils.safestring import mark_safe

from typing import Union

register = template.Library()


@register.simple_tag
def contact_input(index: int = 0, c_val: str = '',
                  hidden: Union[int, str] = ''):
    """ Returns li-tag for ArrayField contacts """

    name = 'name="contacts"' if not hidden else ''

    return mark_safe(f"""
        <li class="array-item row mt-3" name="li_contacts" 
                id="id_li_contacts_{index}" {hidden}>
            <div class="col-10">
                <input type="text" value="{c_val}" maxlength="100"
                    placeholder="Enter your contact" class="form-control" 
                        {name} id="id_contacts_{index}">
            </div>
            <div class="col-1">
                <button type="button" class="btn btn-outline-secondary mb-0" 
                    aria-label="Close" name="del_contact">
                  <span aria-hidden="true">&times;</span>
                </button>
            </div>
        </li>
    """)


@register.simple_tag
def go_to_main_page():
    """ Returns a-tag with link to main page """
    return mark_safe(
        '<a href="/">'
        '   <img src="/static/assets/img/favicon.png" width="48">'
        '</a>'
    )
