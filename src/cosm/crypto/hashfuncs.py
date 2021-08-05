"""Hash functions of Crypto package."""

import hashlib

from _hashlib import HASH  # type: ignore  # pylint: disable=no-name-in-module


def sha256(contents: bytes) -> bytes:
    """
    Get sha256 hash.

    :param contents: bytes contents.

    :return: bytes sha256 hash.
    """
    h: HASH = hashlib.sha256()
    h.update(contents)
    return h.digest()


def ripemd160(contents: bytes) -> bytes:
    """
    Get ripemd160 hash.

    :param contents: bytes contents.

    :return: bytes ripemd160 hash.
    :raises RuntimeError: if hash algorithm is unavailable.
    """
    if "ripemd160" not in hashlib.algorithms_available:
        raise RuntimeError("ripemd160 hash not supported on your platform")

    h: HASH = hashlib.new("ripemd160")
    h.update(contents)
    return h.digest()
