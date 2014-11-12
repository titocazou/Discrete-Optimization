using System;
using System.Collections.Generic;


namespace TravelingSalesman
{
    /// <summary>
    ///   A simple example solver (the same as the one which comes with the assignment)
    /// </summary>
    public class Solver : ISolver
    {
        #region ISolver Members

        public double EnergyFunction(double Energy, double temp)
        {
            return Math.Exp(Energy / temp);
        }

        public void IndexGenerator(ref int index1, ref int index2, int range, Random rand)
        {
            index1 = (int)Math.Floor((range * rand.NextDouble()));

            bool generated = false;

            while (Math.Abs(index1 - index2) <= 1 || generated == false)
            {
                index2 = (int)Math.Floor((range * rand.NextDouble()));
                generated = true;
            }
        }
        public SolutionResult Solve(IEnumerable<Node> nodes)
        {
            SolutionResult sol = new SolutionResult();
            SolutionResult candidate = new SolutionResult();

            /* range represent the number of cities */
            int range = 0;
            int count = 0;
            int count_overall=0;

            int indexAnchor = 0;
            int indexFloater = 0;

            double temp_init = 1000;
            double temp_final = 0.01;
            double total_count = 1e3;
            double temp = temp_init;

            double energy = 0;
            double prob = 0;
            Random rand = new Random();

            double solDistance = 0;
            double minDistance;

            bool solChanged = true;


            /* Get Initial solution by adding nodes naively */
            foreach (Node node in nodes)
            {
                sol.Path.Add(node);
                ++range;
            }

            SolutionResult min = new SolutionResult(sol.Path);
            minDistance = sol.Distance;


            while (temp > temp_final)
            {
                IndexGenerator(ref indexAnchor, ref indexFloater, range, rand);

                if (solChanged)
                {
                    solDistance = sol.Distance;
                    solChanged = false;
                }

                candidate.Path = new List<Node>(sol.Path);
                candidate.Path = _2opt.Switch(indexAnchor, indexFloater, candidate.Path);

                energy = solDistance - candidate.Distance;

                if (energy >= 0)
                {
                    sol.Path = new List<Node>(candidate.Path);
                    solChanged = true;
                }
                else
                {
                    prob = EnergyFunction(energy, temp);

                    if (prob > rand.NextDouble())
                    {
                        sol.Path = new List<Node>(candidate.Path);
                        solChanged = true;
                    }
                }

                if (solDistance < minDistance) min.Path = new List<Node>(sol.Path); minDistance = min.Distance;

                temp = temp_init * Math.Pow(temp_final / temp_init, count / total_count);
                //temp = temp_init - count * (temp_init - temp_final) / total_count;
                    

                ///* Reheat */
                //if (temp < 0.3)
                //{
                //    count = 0;
                //    temp_init = 1000;
                //    temp_final = 0.1;
                //}
             
    



                if (Global.Submit == true) temp = 0;
                ++count;
                ++count_overall;


                if (count_overall % 100 == 0)
                {
                    if (Global.Submit == false)
                    {
                        Console.WriteLine("Current temperature : {0}", temp);
                        Console.WriteLine("Current Minimum : {0}", minDistance);
                        Console.WriteLine("Current Count : {0} \n", count_overall);
                    }

                }
            }


            return min;
        }

        #endregion
    }
}