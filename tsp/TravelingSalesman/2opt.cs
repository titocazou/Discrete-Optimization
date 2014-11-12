using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace TravelingSalesman
{
    /// <summary>
    /// A class allowing to perform a 2-opt operation
    /// </summary>
    public static class _2opt
    {

        public static List<Node> Switch(int anchorIndex, int floaterIndex, List<Node> currentPath)
        {
            int size = currentPath.Count;
            List<Node> core = new List<Node>();

            if (anchorIndex >= size || floaterIndex >= size || Math.Abs(anchorIndex - floaterIndex) <= 1)
            {
                Console.WriteLine("Error in chosen indexes");
                return null;
            }

            int start = Math.Min(anchorIndex, floaterIndex) + 1;
            int count = Math.Abs(anchorIndex - floaterIndex) - 1;

            core = currentPath.GetRange(start, count);
            core.Reverse();

            currentPath.RemoveRange(start, count);

            if (anchorIndex < floaterIndex && core != null)
            {
                currentPath.InsertRange(anchorIndex + 2, core);
            }
            else if (anchorIndex > floaterIndex && core != null)
            {
                currentPath.InsertRange(anchorIndex-count-1, core);
            }


            //StringBuilder builder = new StringBuilder();

            //foreach (Node node in currentPath)
            //    builder.Append(node.Index + " ");

            //Console.WriteLine(builder);
            return currentPath;
        }

    }
}
