{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "source": [
        "num1 = float(input(\"Enter first number: \"))\n",
        "num2 = float(input(\"Enter second number: \"))\n",
        "\n",
        "print(\"Sum =\", num1 + num2)\n",
        "print(\"Difference =\", num1 - num2)\n",
        "print(\"Product =\", num1 * num2)\n",
        "\n",
        "if num2 != 0:\n",
        "    print(\"Quotient =\", num1 / num2)\n",
        "else:\n",
        "    print(\"Cannot divide by zero\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "collapsed": true,
        "id": "cDlZIpTzvGkx",
        "outputId": "b1224160-0882-4bae-97e3-77232eb61471"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter first number: 60\n",
            "Enter second number: 80\n",
            "Sum = 140.0\n",
            "Difference = -20.0\n",
            "Product = 4800.0\n",
            "Quotient = 0.75\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "name = input(\"Enter student name: \")\n",
        "student_id = input(\"Enter student ID: \")\n",
        "age = int(input(\"Enter age: \"))\n",
        "department = input(\"Enter department: \")\n",
        "cgpa = float(input(\"Enter CGPA: \"))\n",
        "\n",
        "print(\"\\n   Student Profile   \")\n",
        "print(\"Name:\", name)\n",
        "print(\"Student ID:\", student_id)\n",
        "print(\"Age:\", age)\n",
        "print(\"Department:\", department)\n",
        "print(\"CGPA:\", cgpa)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "lq_aliM6wbAQ",
        "outputId": "752c5c15-9b6a-4d19-a655-9ae461d9af23"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter student name: Tanvir\n",
            "Enter student ID: 25-62724-2\n",
            "Enter age: 24\n",
            "Enter department: data science\n",
            "Enter CGPA: 3.93\n",
            "\n",
            "   Student Profile   \n",
            "Name: Tanvir\n",
            "Student ID: 25-62724-2\n",
            "Age: 24\n",
            "Department: data science\n",
            "CGPA: 3.93\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "celsius = float(input(\"Enter temperature in Celsius: \"))\n",
        "\n",
        "fahrenheit = (celsius * 9/5) + 32\n",
        "kelvin = celsius + 273.15\n",
        "\n",
        "print(\"Temperature in Fahrenheit =\", fahrenheit)\n",
        "print(\"Temperature in Kelvin =\", kelvin)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "collapsed": true,
        "id": "kdAgAfu9x-qA",
        "outputId": "e5025dc4-f316-4a61-8c8d-388bd4633fd5"
      },
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter temperature in Celsius: 38\n",
            "Temperature in Fahrenheit = 100.4\n",
            "Temperature in Kelvin = 311.15\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "name = input(\"Enter student name: \")\n",
        "\n",
        "m1 = float(input(\"Enter mark 1: \"))\n",
        "m2 = float(input(\"Enter mark 2: \"))\n",
        "m3 = float(input(\"Enter mark 3: \"))\n",
        "m4 = float(input(\"Enter mark 4: \"))\n",
        "m5 = float(input(\"Enter mark 5: \"))\n",
        "\n",
        "total = m1 + m2 + m3 + m4 + m5\n",
        "average = total / 5\n",
        "\n",
        "highest = m1\n",
        "lowest = m1\n",
        "\n",
        "if m2 > highest:\n",
        "    highest = m2\n",
        "if m3 > highest:\n",
        "    highest = m3\n",
        "if m4 > highest:\n",
        "    highest = m4\n",
        "if m5 > highest:\n",
        "    highest = m5\n",
        "\n",
        "if m2 < lowest:\n",
        "    lowest = m2\n",
        "if m3 < lowest:\n",
        "    lowest = m3\n",
        "if m4 < lowest:\n",
        "    lowest = m4\n",
        "if m5 < lowest:\n",
        "    lowest = m5\n",
        "\n",
        "passed = 0\n",
        "if m1 >= 50:\n",
        "    passed = passed + 1\n",
        "if m2 >= 50:\n",
        "    passed = passed + 1\n",
        "if m3 >= 50:\n",
        "    passed = passed + 1\n",
        "if m4 >= 50:\n",
        "    passed = passed + 1\n",
        "if m5 >= 50:\n",
        "    passed = passed + 1\n",
        "\n",
        "print(\"\\n     Student Result    \")\n",
        "print(\"Student Name:\", name)\n",
        "print(\"Total:\", total)\n",
        "print(\"Average:\", average)\n",
        "print(\"Highest:\", highest)\n",
        "print(\"Lowest:\", lowest)\n",
        "print(\"Passed courses:\", passed)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "collapsed": true,
        "id": "_blhN0pRzW-Q",
        "outputId": "94fbb925-443b-4b89-8023-5991edbdc075"
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter student name: karim\n",
            "Enter mark 1: 68\n",
            "Enter mark 2: 69\n",
            "Enter mark 3: 70\n",
            "Enter mark 4: 78\n",
            "Enter mark 5: 88\n",
            "\n",
            "     Student Result    \n",
            "Student Name: karim\n",
            "Total: 373.0\n",
            "Average: 74.6\n",
            "Highest: 88.0\n",
            "Lowest: 68.0\n",
            "Passed courses: 5\n"
          ]
        }
      ]
    }
  ]
}
