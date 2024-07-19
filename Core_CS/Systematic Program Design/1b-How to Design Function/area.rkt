;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname area) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
; Number -> Number
; Area of the square with given one side of a square
(check-expect (area 3) 9)
(check-expect (area 1.2) (* 1.2 1.2))

;(define (area n) 0)

(define (area n)
  (* n n))

