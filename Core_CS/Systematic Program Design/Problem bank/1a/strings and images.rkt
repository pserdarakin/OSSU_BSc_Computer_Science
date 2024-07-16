;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname |strings and images|) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
(require 2htdp/image)
(above (rectangle 60 20 "solid" "red")
       (above (overlay (circle 10 "solid" "yellow") (rectangle 60 20 "solid" "white") )
       (rectangle 60 20 "solid" "green")))