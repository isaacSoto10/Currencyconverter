from flask import Flask, flash

def display_error(error,preface="",postface=""):
    flash(f"{preface} {error} {postface}")