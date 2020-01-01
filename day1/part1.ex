defmodule PartOne do
  def calculateMass(m) do
    div(m, 3) - 2
  end

  def addMass([], acc), do: acc
  def addMass([ mass | tail ], acc), do: addMass(tail, acc + calculateMass(String.to_integer(mass)))

  def part1(input) do
    addMass(readInput(input), 0)
  end

  def readInput(file_name) do
    case File.read(file_name) do
      {:ok, file} ->
	String.split(file, "\n")
      _ ->
	IO.puts "Couldn't read file"
    end
  end
end

defmodule PartTwo do
  def calculateMass(m) do
    fuel = div(m, 3) - 2
    calculateMass(fuel, fuel)
  end
  def calculateMass(m, acc) do
    fuel = div(m, 3) - 2
    if (fuel > 0) do
      calculateMass(fuel, acc + fuel)
    else
      acc
    end
  end

  def addMass([], acc), do: acc
  def addMass([ mass | tail ], acc), do: addMass(tail, acc + calculateMass(String.to_integer(mass)))

  def part2(input) do
    addMass(readInput(input), 0)
  end

  def readInput(file_name) do
    case File.read(file_name) do
      {:ok, file} ->
  String.split(file, "\n")
      _ ->
  IO.puts "Couldn't read file"
    end
  end
end
