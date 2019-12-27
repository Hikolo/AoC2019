defmodule PartOne do
  def calculateMass(m) do
    div(m, 3) - 2
  end

  def addMass([], acc), do: acc
  def addMass([ h| t ], acc), do: addMass(t, acc + calculateMass(String.to_integer(h)))

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
