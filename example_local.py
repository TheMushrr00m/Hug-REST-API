#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Primer método: acceso local"""
import hug


@hug.local()
def say_hello(name: hug.types.text, age: hug.types.number, hug_timer=3):
    """Decimos hola al usuario y muestra su edad"""
    return {
        'message': "Hola {0}, tu edad es de {1} años".format(name, age),
        'took': float(hug_timer)
    }


if __name__ == '__main__':
    print(say_hello("Jhon Doe", 22))