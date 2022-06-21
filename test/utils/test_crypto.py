from merkly.utils.crypto import keccak, slicer, merkle_root
from pytest import mark
from typing import List

@mark.parametrize(
  "data, expect",
  [
    ("string very long", "2b91b0c651a9e25f0c3ca0278fe4ce8d5fae980731bc48f92fa192886d4dc4b6"),
    ("ethereum", "541111248b45b7a8dc3f5579f630e74cb01456ea6ac067d3f4d793245a255155"),
    ("bitcoin", "7dee6e1aa550de37364ec77e03e62ea56bf42037b8297280de9d844d88444e4d"),
    ("merkle", "326fe0d8a70ab934a7bf9d1323c6d87ee37bbe70079f82e72203b1e07c0c185c"),
    ("cars", "0ee92a51567d02169526115460f55ddef86e734b94b947896e82d4532671fdf2"),
    ("tree", "b2510336c6497719adadc7ade198c988520f3349445f074dc729df0f3c2b12ad"),
    ("a", "3ac225168df54212a25c1c01fd35bebfea408fdac2e31ddd6f80a4bbf9a5f1cb"),
    ("b", "b5553de315e0edf504d9150af82dafa5c4667fa618ed0a6f19c69b41166c5510"),
    ("x", "7521d1cadbcfa91eec65aa16715b94ffc1c9654ba57ea2ef1a2127bca1127a83"),
    ("y", "83847cf31c36389df832d0d4d3df7cf28f211e3f83173e5c157bab31573d61f3")
  ]
)
def test_of_keccak(data: str, expect: bool):
  assert expect == keccak(data)



@mark.parametrize(
  "full, half",
  [
    ([i for i in range(2)], 1),
    ([i for i in range(7)], 4),
    ([i for i in range(10)], 5),
    ([i for i in range(112)], 56),
    ([i for i in range(200)], 100),
    ([i for i in range(900)], 450),
    ([i for i in range(1002)], 501),
    ([i for i in range(2040)], 1020),
    ([i for i in range(5008)], 2504),
    ([i for i in range(10010)], 5005)
  ]
)
def test_slicer(full: List[int], half: int):
  assert half == len(slicer(full))


@mark.parametrize(
  "leafs, root",
  [
    (["a", "b", "c", "d", "e", "f", "g", "h", "1","2","3","4","5","6","7","8"], "3818695492749d7eefc6a22cde83b4276263e0597ec86f74bf6d8fc7423f721a"),
    (["a", "b", "c", "d", "e", "f", "g", "h"], "5cf1a5ef31f067f883c20e9dd709b430ae273db5d65f61c1f175bbe7076d3206"),
    (["a", "b", "c", "d"], "159b0d5005a27c97537ff0e6d1d0d619be408a5e3f2570816b02dc5a18b74f47"),
    (["a", "b"], "63a9f18b64ca5a98ad9dba59259edb0710892614501480a9bed568d98450c151"),
    (["a"], "3ac225168df54212a25c1c01fd35bebfea408fdac2e31ddd6f80a4bbf9a5f1cb")
  ]
)
def test_create_root(leafs: List[str], root: str):
  assert merkle_root(leafs) == [root]
