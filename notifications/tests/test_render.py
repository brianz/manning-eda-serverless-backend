import renderer


def test_render():
    order_details = {
        'recipient': 'brianz@gmail.com',
        'order_total': 45.32,
        'first_name': 'Brian',
        'order_id': 333,
    }
    text_body, html_body = renderer.render_new_order(order_details)
    assert 'Brian' in text_body
    assert '45.32' in text_body
    assert '333' in text_body

    assert 'Brian' in html_body
    assert '45.32' in html_body
    assert '333' in html_body