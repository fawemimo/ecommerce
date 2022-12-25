from urllib import response


def test_get_all_categories(c_client, category_with_multiple_children):
    endpoint = "/djninja/inventory/category/all/"
    response = c_client().get(endpoint)
    # assert response.status_code == 200
    # assert len(response.data) == len(category_with_multiple_children)
    response.content
