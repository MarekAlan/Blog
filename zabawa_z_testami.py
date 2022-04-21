from datetime import datetime


# def add(a, b):
#     if a == 50:
#         return 1.2
#     return a + b
#
#
# def test_check_for_0_0():
#     assert add(0,0) == 0 #asercja - stopuje i wywala na błedzie
#
# def test_check_for_0_1():
#     assert add(0, 1) == 1
#
# def test_check_for_0_2():
#     assert add(0, 2) == 2
#
# def test_check_for_0_3():
#     assert add(0, 3) == 3


def analyze_pesel(pesel):
    weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    weight_index = 0
    digits_sum = 0
    for digit in pesel[: -1]:
        digits_sum += int(digit) * weights[weight_index]
        weight_index += 1
    pesel_modulo = digits_sum % 10
    validate = 10 - pesel_modulo
    if validate == 10:
        validate = 0
    gender = "male" if int(pesel[-2]) % 2 != 0 else "female"
    year = pesel[0:2]
    month = int(pesel[2:4])
    if month > 20 and month < 40:
        month -= 20
        year = int('20' + year)
    else:
        year = int("19" + year)
    day = int(pesel[4:6])
    birth_date = datetime(year, month, day)
    result = {
        "pesel": pesel,
        "valid": validate == int(pesel[-1]),
        "gender": gender,
        "birth_date": birth_date
    }
    return result


import pytest


@pytest.mark.parametrize("pesel", [
    '73090992548', '71050733594', '98061671112',
    '89050561165', '03280284755', '98091228249',
    '55040542416', '69110628588', '69081682392', '50051834428'])
def test_check_if_ap_return_correct_pesel(pesel):
    ret_val = analyze_pesel(pesel)
    assert ret_val['pesel'] == pesel


@pytest.mark.parametrize("pesel", [
    '73090992548', '71050733594', '98061671112',
    '89050561165', '03280284755', '98091228249',
    '55040542416', '69110628588', '69081682392', '50051834428'])
def test_check_if_pesel_is_valid(pesel):
    ret_val = analyze_pesel(pesel)
    assert ret_val['valid']  # domyślnie jest is True


@pytest.mark.parametrize("pesel", [
    '73090992542', '71050733593', '98061671114',
    '89050561163', '03280284757', '98091228246',
    '55040542414', '69110628582', '69081682391', '50051834427'])
def test_check_if_pesel_is_not_valid(pesel):
    ret_val = analyze_pesel(pesel)
    assert not ret_val['valid']


@pytest.mark.parametrize("pesel", [
    '90061926254', '36101684773', '36071283655', '28112587811'])
def test_check_gender_male(pesel):
    ret_val = analyze_pesel(pesel)
    assert ret_val['gender'] == 'male'


@pytest.mark.parametrize("pesel", [
    '35042482428', '84032268148', '90050580340', '26040508168'])
def test_check_gender_female(pesel):
    ret_val = analyze_pesel(pesel)
    assert ret_val['gender'] == 'female'


@pytest.mark.parametrize("pesel, bd", [
    ('73090992548', datetime(1973, 9, 9)),
    ('71050733594', datetime(1971, 5, 7)), ])
def test_check_if_ap_pesel_valid(pesel, bd):
    ret_val = analyze_pesel(pesel)
    assert ret_val['birth_date'] == bd
