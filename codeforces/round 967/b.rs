use std::fmt::Display;
use std::io::{stdin, stdout, BufRead, BufReader, BufWriter, Read, Write};

struct IO<Input, Output>
where
    Input: Read,
    Output: Write,
{
    inp: BufReader<Input>,
    out: BufWriter<Output>,
}

#[allow(dead_code)]
impl<Input, Output> IO<Input, Output>
where
    Input: Read,
    Output: Write,
{
    fn new(inp: Input, out: Output) -> Self {
        Self {
            inp: BufReader::new(inp),
            out: BufWriter::new(out),
        }
    }

    fn next<T: std::str::FromStr>(&mut self) -> T {
        let mut line = String::new();
        self.inp.read_line(&mut line).expect("Failed to read line");
        line.trim().parse::<T>().ok().unwrap()
    }

    fn prints(&mut self, items: &[impl Display], sep: &str) {
        writeln!(
            self.out,
            "{}",
            items
                .iter()
                .map(|x| x.to_string())
                .collect::<Vec<_>>()
                .join(sep)
        )
        .ok();
    }
}

fn main() {
    let mut io = IO::new(stdin(), stdout());
    for _ in 0..io.next() {
        let n: usize = io.next::<usize>();
        if n % 2 == 0 {
            println!("-1");
            continue;
        }
        if n == 1 {
            println!("1");
            continue;
        }
        if n < 5 {
            println!("3 1 2");
            continue;
        }
        let mut arr: Vec<i32> = vec![-1; n];
        let mid: usize = n / 2;
        arr[mid] = 1;
        arr[mid + 1] = 2;
        arr[mid - 1] = 3;
        let mut last = 2;
        let mut one = false;
        for i in mid + 2..n {
            if one {
                arr[i] = last + 1;
                last = arr[i];
            } else {
                arr[i] = last + 3;
                last = arr[i];
            }
            one = !one;
        }

        last = 3;
        one = true;
        for i in (0..mid - 1).rev() {
            if !one {
                arr[i] = last + 3;
                last = arr[i];
            } else {
                arr[i] = last + 1;
                last = arr[i];
            }
            one = !one;
        }
        // println!("{:?}", arr);
        io.prints(&arr, " ");
        io.out.flush().unwrap();
    }
    return;
}
