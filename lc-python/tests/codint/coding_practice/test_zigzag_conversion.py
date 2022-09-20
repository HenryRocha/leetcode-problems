import pytest
from lc_python.codint.coding_practice.n0006_zigzag_conversion import SOLUTIONS


@pytest.fixture(params=SOLUTIONS)
def implementation(request):
    return request.param


def _check(s, num_rows, expected, solution: object):
    ret = solution().convert(s, num_rows)
    assert ret == expected, f'Wrong answer for input "{s}", {num_rows}'


def test_1(implementation):
    _check("", 0, "", implementation)


def test_2(implementation):
    s = "abcdefghijklmnopqrstuvwxyz"
    _check(s, 1, s, implementation)


def test_3(implementation):
    s = "abcdefghijklmnopqrstuvwxyz"
    e = "acegikmoqsuwybdfhjlnprtvxz"
    _check(s, 2, e, implementation)


def test_4(implementation):
    s = "abcdefghijklmnopqrstuvwxyz"
    e = "aeimquybdfhjlnprtvxzcgkosw"
    _check(s, 3, e, implementation)


def test_5(implementation):
    s = "abcdefghijklmnopqrstuvwxyz"
    e = "agmsybfhlnrtxzceikoquwdjpv"
    _check(s, 4, e, implementation)


def test_6(implementation):
    s = "abcdefghijklmnopqrstuvwxyz"
    e = "aiqybhjprxzcgkoswdflntvemu"
    _check(s, 5, e, implementation)


def test_7(implementation):
    s = "abcdefghijklmnopqrstuvwxyz"
    e = "akubjltvcimswdhnrxegoqyfpz"
    _check(s, 6, e, implementation)


def test_8(implementation):
    s = "abcdefghijklmnopqrstuvwxyz"
    e = "amyblnxzckowdjpveiqufhrtgs"
    _check(s, 7, e, implementation)


def test_9(implementation):
    s = "abcdefghijklmnopqrstuvwxyz"
    e = "aobnpcmqdlrzeksyfjtxgiuwhv"
    _check(s, 8, e, implementation)


def test_10(implementation):
    s = "abcdefghijklmnopqrstuvwxyz"
    e = "aqbprcosdntemuflvgkwhjxziy"
    _check(s, 9, e, implementation)


def test_11(implementation):
    s = "abcdefghijklmnopqrstuvwxyz"
    e = "asbrtcqudpveowfnxgmyhlzikj"
    _check(s, 10, e, implementation)


def test_12(implementation):
    s = "abcdefghijklmnopqrstuvwxyz"
    e = "aubtvcswdrxeqyfpzgohnimjlk"
    _check(s, 11, e, implementation)


def test_13(implementation):
    s = "abcdefghijklmnopqrstuvwxyz"
    e = "awbvxcuydtzesfrgqhpiojnkml"
    _check(s, 12, e, implementation)


def test_14(implementation):
    s = "abcdefghijklmnopqrstuvwxyz"
    e = "aybxzcwdveuftgshriqjpkolnm"
    _check(s, 13, e, implementation)


def test_15(implementation):
    s = "abcdefghijklmnopqrstuvwxyz"
    e = "abzcydxewfvguhtisjrkqlpmon"
    _check(s, 14, e, implementation)


def test_16(implementation):
    s = "abcdefghijklmnopqrstuvwxyz"
    e = "abcdzeyfxgwhviujtkslrmqnpo"
    _check(s, 15, e, implementation)


def test_17(implementation):
    s = "abcdefghijklmnopqrstuvwxyz"
    e = "abcdefzgyhxiwjvkultmsnroqp"
    _check(s, 16, e, implementation)


def test_18(implementation):
    s = "abcdefghijklmnopqrstuvwxyz"
    e = "abcdefghziyjxkwlvmuntosprq"
    _check(s, 17, e, implementation)


def test_19(implementation):
    s = "abcdefghijklmnopqrstuvwxyz"
    e = "abcdefghijzkylxmwnvouptqsr"
    _check(s, 18, e, implementation)


def test_20(implementation):
    s = "abcdefghijklmnopqrstuvwxyz"
    e = "abcdefghijklzmynxowpvqurts"
    _check(s, 19, e, implementation)


def test_21(implementation):
    s = "abcdefghijklmnopqrstuvwxyz"
    e = "abcdefghijklmnzoypxqwrvsut"
    _check(s, 20, e, implementation)


def test_22(implementation):
    s = "abcdefghijklmnopqrstuvwxyz"
    e = "abcdefghijklmnopzqyrxswtvu"
    _check(s, 21, e, implementation)


def test_23(implementation):
    s = "abcdefghijklmnopqrstuvwxyz"
    e = "abcdefghijklmnopqrzsytxuwv"
    _check(s, 22, e, implementation)


def test_24(implementation):
    s = "abcdefghijklmnopqrstuvwxyz"
    e = "abcdefghijklmnopqrstzuyvxw"
    _check(s, 23, e, implementation)


def test_25(implementation):
    s = "abcdefghijklmnopqrstuvwxyz"
    e = "abcdefghijklmnopqrstuvzwyx"
    _check(s, 24, e, implementation)


def test_26(implementation):
    s = "abcdefghijklmnopqrstuvwxyz"
    e = "abcdefghijklmnopqrstuvwxzy"
    _check(s, 25, e, implementation)


def test_27(implementation):
    s = "abcdefghijklmnopqrstuvwxyz"
    e = "abcdefghijklmnopqrstuvwxyz"
    _check(s, 26, e, implementation)


def test_28(implementation):
    s = "abcdefghijklmnopqrstuvwxyz"
    e = "abcdefghijklmnopqrstuvwxyz"
    _check(s, 27, e, implementation)


def test_29(implementation):
    s = "abcdefghijklmnopqrstuvwxyz"
    e = "abcdefghijklmnopqrstuvwxyz"
    _check(s, 100, e, implementation)
