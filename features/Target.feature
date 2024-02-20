# Created by alberthembd at 2/15/24
Feature: Click on empty cart
  Open Target web page; click Cart Icon
  Verify that 'Your Cart is empty' message appears.

  Scenario: Open Target web page and click on Cart Icon with no items in it.
      Given Google Chrome is open and the user has navigated to the Target webpage
      When the user clicks on the cart icon without having put any items into it
      Then Your cart is empty message appears